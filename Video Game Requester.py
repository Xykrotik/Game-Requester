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
        