def mediana(nums1, nums2):
    logicali_laba013 = nums1 + nums2
    logicali_laba013.sort()
    withoutlogical = len(logicali_laba013)
    if withoutlogical % 2 == 0:
        mediana = (logicali_laba013[withoutlogical // 2 - 1] + logicali_laba013[withoutlogical // 2]) / 2
    else:
        mediana = logicali_laba013[withoutlogical // 2]
    return format(mediana, '.5f')

mediana(nums1,nums2)
