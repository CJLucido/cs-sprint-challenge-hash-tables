# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # all_file_paths =[]
    # all_file_paths = {}
    # new_dict = {}
    desired_paths = {}
    undesired_paths = {}
    result = []
    desired_keys = {}
    i = 0
    k = 0

    for query in queries:
        desired_keys[query] = 1

    for file in files:
        files_split = file.rsplit("/", 1)
 
        # if files_split[-1] in undesired_paths.keys():

        #         pass
        # elif files_split[-1] not in desired_keys:
        #             undesired_paths[files_split[-1]] = None
        #             k +=1
        #             print("k", k)
        #             print(k/100000)
        #             # # print(files_split[-1])
        #             # print(undesired_paths)
        
        if desired_keys.get(files_split[-1]) == 1:
                result.append(file)
                # desired_paths[i] = file
                i += 1
                print(i)
                print("result", len(result))


    #----------------------
    # for file in files:
    #     files_split = file.rsplit("/", 1)
    #     for query in queries:
    #         if files_split[-1] in undesired_paths.keys():
    #         # if undesired_paths.get(files_split[-1]):
    #             pass
    #         elif files_split[-1] != query:
    #                 undesired_paths[files_split[-1]] = None
    #                 k +=1
    #                 print("k", k)
    #                 print(k/100000)
    #                 # # print(files_split[-1])
    #                 # print(undesired_paths)
    #     for query in queries:
    #         if files_split[-1] == query:
    #             desired_paths[i] = file
    #             i += 1
    #             print(i)
                #-------------------------
            # else:
            #     print("eliminating")
            #     pass
        #         all_file_paths[file] = [file, files_split]
        # print("all files to set")
        # for item in all_file_paths:
            # result.append(all_file_paths[file][0])
    # for k in range(0, i):
    #     result.append(desired_paths[k])
    #     print("appending")
    #     # for query in queries:
          
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
    # print("result", result)

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
