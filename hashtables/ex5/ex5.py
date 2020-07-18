# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # all_file_paths =[]
    all_file_paths = {}
    # new_dict = {}
    result = []
    i = 0
    for file in files:
        files_split = file.rsplit("/", 1)
        for query in queries:
            if files_split[-1] != query:
                pass
            else:
        #         all_file_paths[file] = [file, files_split]
        # print("all files to set")
        # for item in all_file_paths:
            # result.append(all_file_paths[file][0])
                result.append(file)
                i+=1
                print(i)
        # for query in queries:
          
            # if all_file_paths[file][1][-1] == query:
            #         print("hit")
            #         # print("filessplit", files_split) Spliting at last occurence
            #         result.append(file)
    # print("all_file_paths appended")
    print("results completed")

#----------------------------------
    # for file in files:
    #     files_split = file.split("/")
    #     all_file_paths.append(files_split)

    # print("all_file_paths appended")
    #------------------------------------------

    #ON THE FIRST GO AROUND WE SOMEHOW WANT TO CAPTURE EVERYTHING TO MAKE THIS FASTER

    # for query in queries:
    #     # new_dict[query] = []
    #     for every_array in all_file_paths:
    #         if every_array[-1] == query:
    #             # new_dict[query].append(every_array)
    #             result.append("/".join(every_array))
    #             # "/".join(every_array)
    #             # result.append(every_array)
    #         else:
    #             pass
    # print("all joined")

    #----------------------------------------------
    #     for query in queries:
    #     # new_dict[query] = []
    #     for every_array in all_file_paths:
    #         if every_array[-1] == query:
    #             # new_dict[query].append(every_array)
    #             result.append("/".join(every_array))
    #             # "/".join(every_array)
    #             # result.append(every_array)
    #         else:
    #             pass
    # print("all joined")
    #-----------------------------------------
    # print("new_dict", new_dict)

    # for query in queries:
    #     for path_arr in new_dict[query]:
    #         print("result", result)
    #         result.append("/".join(path_arr))
    
    # for resulting_string in result:
    #     if len(resulting_string) < 1:
    #         result.remove(resulting_string)
    #     else:
    #         pass
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
