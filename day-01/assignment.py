import psutil


def get_cpu_threshold():
    cpu_threshold = int(input("enter the CPU threshould"))

    current_cpu = psutil.cpu_percent(interval=1)
    print("Current CPU%:",current_cpu)
    if current_cpu > cpu_threshold:
        print("CPU Alert Email Sent...")

    else:
        print("CPU is sae state..")


get_cpu_threshold()