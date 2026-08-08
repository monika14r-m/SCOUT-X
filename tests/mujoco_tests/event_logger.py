import datetime

LOG_FILE = "events.log"

def log_event(level, message):

    timestamp = datetime.datetime.now()

    entry = (
        f"[{timestamp}] "
        f"[{level}] "
        f"{message}\n"
    )

    with open(LOG_FILE, "a") as file:
        file.write(entry)

    print(entry.strip())


if __name__ == "__main__":

    log_event(
        "INFO",
        "Patrol started"
    )

    log_event(
        "ALERT",
        "Intruder detected"
    )
