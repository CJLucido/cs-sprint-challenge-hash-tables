# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    all_file_paths =[]
    new_dict = {}
    result = []

    for file in files:
        files_split = file.split("/")
        all_file_paths.append(files_split)
        # print(all_file_paths)

    for query in queries:
        new_dict[query] = []
        for every_array in all_file_paths:
            if every_array[-1] == query:
                new_dict[query].append(every_array)
            else:
                pass
    # print("new_dict", new_dict)

    for query in queries:
        for path_arr in new_dict[query]:
            # print("path", path_arr)
            print("result", result)
            result.append("/".join(path_arr))
    
    for resulting_string in result:
        if len(resulting_string) < 1:
            result.remove(resulting_string)
        else:
            pass
    print("result", result)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
