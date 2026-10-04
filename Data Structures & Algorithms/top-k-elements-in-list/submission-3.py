class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #building the freq_dict array->using that to build the bucket list where index is the count and element is the sublist of elements
        freq_dict={}
        for i in nums:
            if i in freq_dict:
                freq_dict[i]+=1
            else:
                freq_dict[i]=1
        
        buckets=[]
        for i in range(len(nums)+1):
            buckets.append([])
        
        #populating the buckets
        for elem,count in freq_dict.items():
            buckets[count].append(elem)

        result=[]
        for i in range(len(buckets)-1,-1,-1):
            if k-len(result)==0:
                return result
            elif len(buckets[i])>=k:
                result.extend(buckets[i][:k-len(result)])
            else:
                result.extend(buckets[i])
        return result