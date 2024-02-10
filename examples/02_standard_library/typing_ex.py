from typing import List, Union, Optional, Dict

def greet_all(names: List[str]) -> None:
    for name in names:
        print("Hello", name)

def process_data(data: Union[int, str]) -> Union[str, None]:
    if isinstance(data, int):
        return str(data)
    elif isinstance(data, str):
        return data
    return None

def get_user(id: int) -> Optional[Dict[str, str]]:
    if id == 1:
        return {"name": "John", "age": "30"}
    return None
