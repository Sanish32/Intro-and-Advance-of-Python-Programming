    my_file.write(f"{new[0]},{new[1]} credits\n")
        my_file.write("======================================\n")
        my_file.write(f"{word1:30}{word2:<10}{word3:<10}{word4:<10}{word5:<10}{word6}\n")
        for id,name in dict1.items():
            if id in dict2 and id in dict3:
                j=10
                for i in range(40,4,-4):
                    if dict2[id]==0:
                        points=0
                        break
                    elif dict2[id]>i-1:
                        points=j
                        break
                    j-=1
                abc=dict3[id]+points
                
                if abc>=27:
                        g=5
                elif abc>23:
                    g=4
                elif abc>20:
                    g=3
                elif abc>17:
                    g=2
                elif abc>14:
                    g=1
                else:
                    g=0
                my_file.write(f"{name:30}{dict2[id]:<10}{points:<10}{dict3[id]:<10}{abc:<10}{g}\n")
                
                new_file.write(f"{name};"+"{g}")