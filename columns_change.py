df[column_to_edit] = df[column_to_edit].apply(lambda x: '_'.join(x.split('_')[:2] + [df[insert_column][df[column_to_edit] == x].iloc[0]] + x.split('_')[3:]))
