""" Entrypoint for 2026ObjectDetection """
import src.network_tables as nt


def main() -> None:
    """ Main function """
    network_tables = nt.NetworkTables(is_host=True)



if __name__ is "__main__":
    main()
