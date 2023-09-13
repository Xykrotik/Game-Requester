# Initialize an empty list to store game requests
game_requests = []

# Function to add a game request
def add_request():
    title = input("Enter the title of the game: ")
    platform = input("Enter the platform (e.g., PC, PS4, Xbox): ")
    release_date = input("Enter the release date: ")
    
    # Create a dictionary to represent the request
    request = {
        "title": title,
        "platform": platform,
        "release_date": release_date
        
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
            
# Main loop
while True:
    print("\n==== Game Request System ====")
    print("1. Add Game Request")
    print("2. View Game Requests")
    print("3. Exit")
    
    choice = input("Select an option (1/2/3): ")
    
    if choice == "1":
        add_request()
    elif choice == "2":
        view_requests()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")
        
        