def write_user_usage(username, user_type, function):
    from datetime import datetime

    now = datetime.now()
    # Change format to "YYYY-MM-DD HH:MM:SS"
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    log_list = []
    log_list.append([formatted_datetime, username, user_type, function, "\n"])
    with open("user_usage.txt", "w") as user_usage:
        for record in log_list:
            recordString = ",".join(record)
            user_usage.write(recordString)
