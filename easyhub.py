import psutil
import platform
from datetime import datetime
import tabulate
import time

class EasyHub:
    def __init__(self):
        self.system_info = self.get_system_info()
    
    def get_system_info(self):
        uname = platform.uname()
        return {
            "System": uname.system,
            "Node Name": uname.node,
            "Release": uname.release,
            "Version": uname.version,
            "Machine": uname.machine,
            "Processor": uname.processor
        }
    
    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)
    
    def get_memory_usage(self):
        mem = psutil.virtual_memory()
        return {
            'Total': mem.total,
            'Available': mem.available,
            'Used': mem.used,
            'Percentage': mem.percent
        }
    
    def get_disk_usage(self):
        partitions = psutil.disk_partitions()
        usage_data = []
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            usage_data.append({
                "Device": partition.device,
                "Mountpoint": partition.mountpoint,
                "File System Type": partition.fstype,
                "Total Size": usage.total,
                "Used": usage.used,
                "Free": usage.free,
                "Percentage": usage.percent
            })
        return usage_data
    
    def get_task_info(self):
        tasks = []
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                tasks.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return tasks
    
    def display_system_info(self):
        print("System Information:")
        for key, value in self.system_info.items():
            print(f"{key}: {value}")
    
    def display_usage_stats(self):
        print("\nCPU Usage: {:.2f}%".format(self.get_cpu_usage()))
        
        memory = self.get_memory_usage()
        print("Memory Usage:")
        for key, value in memory.items():
            print(f"  {key}: {value}")
        
        print("\nDisk Usage:")
        usage_data = self.get_disk_usage()
        print(tabulate.tabulate(usage_data, headers="keys"))
    
    def display_task_info(self):
        tasks = self.get_task_info()
        print("\nRunning Tasks:")
        print(tabulate.tabulate(tasks, headers="keys"))
    
    def start(self):
        self.display_system_info()
        while True:
            self.display_usage_stats()
            self.display_task_info()
            print("\nUpdating in 5 seconds...\n")
            time.sleep(5)

if __name__ == "__main__":
    easyhub = EasyHub()
    easyhub.start()