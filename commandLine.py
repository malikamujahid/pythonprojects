import json
import logging
import argparse

filename = "activity.json"
logging.basicConfig(level=logging.INFO, format='%(message)s')

activity_list = []

def loadActivity(filename):
    global activity_list
    logging.info("Loading activity list from file in load activity function.")
    try:
        with open(filename, mode='r') as f:
            activity_list = json.load(f)
            logging.info("Activity list loaded successfully.")
    except FileNotFoundError:
        print("File not found IN load activity function.") 

def writeActivity(filename):
    global activity_list
    logging.info("Writing activity list to file in write activity function.")
    print(activity_list)
    with open(filename, 'w') as f:
        json.dump(activity_list, f, indent=4)
        logging.info("Activity list written successfully in write activity function.")

def appendActivity(activity_toAdd, status):
    global activity_list
    logging.info(f"Appending activity '{activity_toAdd}' with status '{status}' in append function.")
    max_id = max([item['activity_id'] for item in activity_list], default=0)
    new_id = max_id + 1

    if activity_toAdd not in [item['activity'] for item in activity_list]:
        logging.info(f"Activity '{activity_toAdd}' does not exist. Adding new activity using append activity function.")
        activity_list.append({
            'activity_id': new_id,
            'activity': activity_toAdd,
            'status': status
        })
    else:
        logging.warning(f"Activity '{activity_toAdd}' already exists. Not adding duplicate.")

def addActivity(activity, status, filename):
    global activity_list
    print("hi")
    logging.info(f"Adding activity '{activity}' with status '{status}'.")
    loadActivity(filename)
    logging.info("Current activity list loaded.")
    appendActivity(activity, status)
    logging.info("Activity appended to the list.")
    writeActivity(filename)
    logging.info("Activity list written to file successfully in add activity function.")

def deleteActivity(activityDelete, filename):
    global activity_list
    logging.info(f"Deleting activity '{activityDelete}' using delete function.")
    loadActivity(filename)
    logging.info("Current activity list loaded. for deleteActivity.")
    activity_list[:] = [item for item in activity_list if item['activity'] != activityDelete]
    writeActivity(filename)
    """logging.info(f"Activity '{activityDelete}' deleted successfully using delete function.") """

def updateStatus(status, activity_id, filename):
    global activity_list
    logging.info(f"Updating status using update function")
    loadActivity(filename)
    for item in activity_list:
        if item['activity_id'] == activity_id:
            item['status'] = status
    writeActivity(filename)
    logging.info(f"Status of activity ID {activity_id} updated to '{status}' successfully using update status function.")

def main():
    parser = argparse.ArgumentParser(description="Manage activities.")
    parser.add_argument('command', choices=['add', 'delete', 'update'], help="Command to execute.")
    parser.add_argument('activity', help="Activity name or ID (for update).")
    parser.add_argument('status', choices=['not started', 'in progress', 'completed'], help="Status to set.")
    parser.add_argument('--filename', default='activity.json', help="Filename to store activities.")

    args = parser.parse_args()
    print(args)

    if args.command == 'add':
        addActivity(args.activity, args.status, args.filename)

    elif args.command == 'delete':
        deleteActivity(args.activity, args.filename)

    elif args.command == 'update':
        try:
            activity_id = int(args.activity)
        except ValueError:
            print("Error: For update, 'activity' must be an activity ID (integer).")
            return
        updateStatus(args.status, activity_id, args.filename)

if __name__ == "__main__":
    main()