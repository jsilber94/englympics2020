from weighted_levenshtein import lev, osa, dam_lev


def match(str1, str2, transpose_costs, substitute_costs, delete_costs, insert_costs):
    # Testing
    print(dam_lev('ABNANA', 'BANANA', transpose_costs=transpose_costs, substitute_costs=substitute_costs,
              delete_costs=delete_costs, insert_costs=insert_costs))

