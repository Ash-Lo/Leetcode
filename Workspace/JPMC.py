# import collections
#
# line = 'veiifogvweesotwnetnvfeheiot\n'
# val = line[0:len(line)-1]
# ref_dict = {'z':0, 'w':2, 'g':8, 'x':6, 'v':5, 'o':1, 's':7, 'f':4, 'h':3, 'i':9}
# res = [0]*10
# #print(ref_dict)
#
# for letter in val:
#     if letter in ref_dict.keys():
#         res[ref_dict[letter]] += 1
#
# res[7] -= res[6]
# res[5] -= res[7]
# res[4] -= res[5]
# res[1] -= (res[2] + res[4] + res[0])
# res[3] -= res[8]
# res[9] -= (res[5] + res[6] + res[8])
## print(res)
# fin = ''
# for i,val in enumerate(res):
#     if val:
#         fin += str(i)*val
# print(fin)
import collections

str = "onetwothreefourfivesixseveneightnine"

freq = collections.Counter(str)
print(freq)