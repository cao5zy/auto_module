import sys
from yaml import load

def get_config_path ():
    return sys.argv[1]


def main():
    print(get_config_path())
    with open(get_config_path(), 'r', encoding='utf-8') as yaml_file:
        yaml_content = load(yaml_file)
        print(yaml_content)
        
    

if __name__ == '__main__':
    main()
