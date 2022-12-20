from utils import read_data
from string import ascii_lowercase, ascii_uppercase

PRIORITIES = {
   l: i + 1 for i, l in enumerate(ascii_lowercase)
}
PRIORITIES.update({
   l: i + 27 for i, l in enumerate(ascii_uppercase)
})
