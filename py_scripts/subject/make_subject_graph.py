import get_data as gd
import get_subjects as gs

list_of_dicts = gd.get_data_list_of_dicts()

subject_list = gs.get_subjects(list_of_dicts)
