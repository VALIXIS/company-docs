import time
import winrm
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

REMOTE_IP = "100.127.80.62"

def is_online(ip):
    try:
        res = subprocess.run(["ping", "-n", "1", "-w", "1000", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return res.returncode == 0
    except Exception:
        return False

def kill_daemon():
    logging.info(f"Connecting to {REMOTE_IP} via WinRM to kill lead_engine_daemon...")
    try:
        s = winrm.Session(f'http://{REMOTE_IP}:5985/wsman', auth=('antigravity', 'Valixis2026!'), transport='ntlm')
        ps = """
        Get-CimInstance Win32_Process -Filter "Name = 'python.exe'" | Where-Object { $_.CommandLine -like '*lead_engine_daemon*' } | ForEach-Object { 
            Write-Host "Killing PID $($_.ProcessId)"
            Stop-Process -Id $_.ProcessId -Force 
        }
        Stop-ScheduledTask -TaskName ValixisOutboundDaemon -ErrorAction SilentlyContinue
        Disable-ScheduledTask -TaskName ValixisOutboundDaemon -ErrorAction SilentlyContinue
        Write-Host "ValixisOutboundDaemon disabled successfully."
        """
        r = s.run_ps(ps)
        logging.info("STDOUT: " + r.std_out.decode('utf-8', errors='ignore'))
        logging.info("STDERR: " + r.std_err.decode('utf-8', errors='ignore'))
        
        # Copy the updated files over SMB
        subprocess.run(f'copy ai_agents\\linkedin_queue.py \\\\{REMOTE_IP}\\c$\\Valixis\\ai_agents\\linkedin_queue.py /Y', shell=True)
        subprocess.run(f'copy ai_agents\\whatsapp_client.py \\\\{REMOTE_IP}\\c$\\Valixis\\ai_agents\\whatsapp_client.py /Y', shell=True)
        logging.info("Updated linkedin_queue.py and whatsapp_client.py copied to subhash-pc.")
        return True
    except Exception as e:
        logging.error(f"Error during remote kill: {e}")
        return False

if __name__ == "__main__":
    logging.info("Waiting for subhash-pc (100.127.80.62) to come online...")
    # Attempt once immediately or check ping
    if is_online(REMOTE_IP):
        kill_daemon()
    else:
        logging.info("subhash-pc is currently offline. Daemon watcher will keep checking in background.")
        for _ in range(60): # 10 minutes
            time.sleep(10)
            if is_online(REMOTE_IP):
                logging.info("subhash-pc came online! Triggering termination...")
                if kill_daemon():
                    break
