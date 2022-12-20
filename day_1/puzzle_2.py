from .common import get_elf_calories


def execute():
    return sum(sorted(get_elf_calories(), reverse=True)[:3])
