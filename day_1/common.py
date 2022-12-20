from utils import read_data


def get_elf_calories():
    elf_inventory = []
    elf_inventory.append([])
    # Elf inventories are seperated by two empty lines.
    for row in read_data(1):
        stripped = row.strip()
        if stripped:
            elf_inventory[-1].append(int(stripped))
            continue
        if not elf_inventory[-1]:
            continue
        elf_inventory.append([])

    return [sum(inv) for inv in elf_inventory]
