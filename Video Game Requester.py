# Initialize an empty list to store game requests
game_requests = []

# Function to display fulfillment status
def fulfilled_status(request):
    if request["fulfilled"]:
        return "Fulfilled"
    else:
        return "Not Fulfilled"

# Function to add a game request
def add_request():
    title = input("Enter the title of the game: ")
    platform = input("Enter the platform (e.g., PC, PS4, Xbox): ")
    release_date = input("Enter the release date: ")
    
    # Create a dictionary to represent the request
    request = {
        "title": title,
        "platform": platform,
        "release_date": release_date,
        "fulfilled": False # Default status is "Not Fulfilled"
        
    }
    
    game_requests.append(request)
    print("Request added successfully!")
    
    
# Function to view all game requests
def view_requests():
    if not game_requests:
        print("No requests yet.")
        return
        
    print("\n--- Game Requests ---")
    for idx, request in enumerate(game_requests, start=1):
        print(f"{idx}. Title: {request['title']}")
        print(f"   Platform: {request['platform']}")
        print(f"   Release Date: {request['release_date']}\n")
        print(f"   Status: {fulfilled_status(request)}\n")

# Function to mark game requests as fulfilled
def mark_fulfilled():
    view_requests()
    if not game_requests:
        return
    
    request_numbers = input("Enter the number of the requests to mark as fulfilled (using commas): ")
    request_numbers = request_numbers.split(',')
    
    marked_requests = [] # To keep track of successfully marked requests
    
    for request_number in request_numbers:
        try:
            request_number = int(request_number.strip()) # Convert to interger
            if 1<= request_number <= len(game_requests):
                game_requests[request_number - 1]["fulfilled"] = True
                marked_requests.append(request_number)
            else:
                print(f"Invalid request number: {request_number}")
        except ValueError:
            print("Invalid input: {request_number} is not a valid request number.")
    
    if marked_requests:
        print(f"Request(s) {', '.join(map(str, marked_requests))} marked as fulfilled.")
        
            
# Main loop
while True:
    print("\n==== Game Request System ====")
    print("1. Add Game Request")
    print("2. View Game Requests")
    print("3. Mark Request as Fulfilled")
    print("4. Exit")
    
    choice = input("Select an option (1 - 4): ")
    
    if choice == "1":
        add_request()
    elif choice == "2":
        view_requests()
    elif choice == "3":
        mark_fulfilled()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1 - 4).")
        
        