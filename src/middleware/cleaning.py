
def clean_path(websocket):
    root_path = websocket.path.split('?')[0]
    websocket.path = root_path
