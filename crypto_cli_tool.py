from cli import create_parser, handle_command

def main():
    parser = create_parser()
    args = parser.parse_args()
    handle_command(args)

if __name__ == "__main__":
    main()
