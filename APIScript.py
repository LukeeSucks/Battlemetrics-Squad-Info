import requests

def get_server_info(server_id, api_key):
    url = f"https://api.battlemetrics.com/servers/{server_id}"
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data")
        return None

def parse_server_info(json_data):
    # Assuming json_data is the direct response from get_server_info
    data = json_data.get('data', {})
    attributes = data.get('attributes', {})
    details = attributes.get('details', {})
    relationships = data.get('relationships', {})

    # Basic information
    server_id = attributes.get('id')
    server_name = attributes.get('name')
    address = attributes.get('address')
    ip = attributes.get('ip')
    port = attributes.get('port')
    players = attributes.get('players')
    max_players = attributes.get('maxPlayers')
    rank = attributes.get('rank')
    location = attributes.get('location')
    status = attributes.get('status')
    private = attributes.get('private')
    created_at = attributes.get('createdAt')
    updated_at = attributes.get('updatedAt')
    port_query = attributes.get('portQuery')
    country = attributes.get('country')
    query_status = attributes.get('queryStatus')

    # Details information
    map_name = details.get('map')
    game_mode = details.get('gameMode')
    version = details.get('version')
    licensed_server = details.get('licensedServer')
    license_id = details.get('licenseId')
    password = details.get('password')
    squad_player_reserve_count = details.get('squad_playerReserveCount')
    squad_play_time = details.get('squad_playTime')
    squad_public_queue_limit = details.get('squad_publicQueueLimit')
    squad_public_queue = details.get('squad_publicQueue')
    squad_reserved_queue = details.get('squad_reservedQueue')
    squad_team_one = details.get('squad_teamOne')
    squad_team_two = details.get('squad_teamTwo')
    squad_next_layer = details.get('squad_nextLayer')

    # Relationships
    game_type = relationships.get('game', {}).get('data', {}).get('type')
    game_id = relationships.get('game', {}).get('data', {}).get('id')

    # Printing all variables
    print(f"Server ID: {server_id}")
    print(f"Server Name: {server_name}")
    print(f"Address: {address}")
    print(f"IP: {ip}")
    print(f"Port: {port}")
    print(f"Players: {players}")
    print(f"Max Players: {max_players}")
    print(f"Rank: {rank}")
    print(f"Location: {location}")
    print(f"Status: {status}")
    print(f"Private: {private}")
    print(f"Created At: {created_at}")
    print(f"Updated At: {updated_at}")
    print(f"Port Query: {port_query}")
    print(f"Country: {country}")
    print(f"Query Status: {query_status}")
    print(f"Map Name: {map_name}")
    print(f"Game Mode: {game_mode}")
    print(f"Version: {version}")
    print(f"Licensed Server: {licensed_server}")
    print(f"License ID: {license_id}")
    print(f"Password: {password}")
    print(f"Squad Player Reserve Count: {squad_player_reserve_count}")
    print(f"Squad Play Time: {squad_play_time}")
    print(f"Squad Public Queue Limit: {squad_public_queue_limit}")
    print(f"Squad Public Queue: {squad_public_queue}")
    print(f"Squad Reserved Queue: {squad_reserved_queue}")
    print(f"Squad Team One: {squad_team_one}")
    print(f"Squad Team Two: {squad_team_two}")
    print(f"Squad Next Layer: {squad_next_layer}")
    print(f"Game Type: {game_type}")
    print(f"Game ID: {game_id}")

    return locals()  # Returns all local variables as a dictionary

def main():
    api_key = 'API_TOKEN'  # Replace with your BattleMetrics API key
    server_id = input("Enter the server identifier: ")
    server_info_json = get_server_info(server_id, api_key)

    if server_info_json:
        server_info = parse_server_info(server_info_json)

        # Example of accessing specific information
        # You can access any data like this:
        # print(f"Specific Data: {server_info['<variable_name>']}")


if __name__ == "__main__":
    main()
