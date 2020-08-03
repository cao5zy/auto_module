import sys
import yaml

def get_config_path (): sys.argv[1]


def main():
    with open(get_config_path(), 'r', encoding='utf-8') as yaml_file:
        yaml_content = yaml.load(yaml_file.read())
        
    

if __name__ == '__main__':
    main()
