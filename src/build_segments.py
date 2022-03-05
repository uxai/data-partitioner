import math

def segment_builder(arg, tail):
    req_list = arg[0]
    divisions = arg[1]
    division_dec = divisions / 100
    # number of segments to be created in the element passed
    partition_count = int(math.ceil(100 / divisions))
    
    if len(arg) == 3:
        segments = arg[2]
    else:
        g = int(100 / divisions + 1)
        segments = tuple([n for n in range(1, g)])

    def builder(segments):
        """
        Calculate the remainder of numbers that won't be evenly split
        into groups, and calculates at which point the groups need to start
        catering for the extra numbers.

        Extra numbers are divided up into the last groups of the list given.
        For example: if we have a list of [1, 2, 3, 4, 5] and we ask to split
        the group in thirds, the ouput would be [1][2, 3][4, 5]
        """
        remainder = int(len(req_list) % partition_count)

        """
        Removes the remainder from the length of the passed in list, this way
        we can continue with an even division. math.floor is used for precaution only.
        """
        partition_size = math.floor(division_dec * (len(req_list)  - remainder))
        segment_storage = []
        if remainder > 0:
            """
            Calculates the number of extras from the length of the list passed.
            Group extras: tells us when to start adding the extras to generated segments
            """
            group_extras = partition_count - remainder

            pos = 0 # keep track of position
            if tail == False:
                cycle = reversed(range(0, partition_count))
            else:
                cycle = range(0, partition_count)
            for group in cycle:
                if group < group_extras:
                    segment_storage.append([pos, pos + partition_size])
                    pos += partition_size
                else:
                    segment_storage.append([pos, pos + partition_size + 1])
                    pos += partition_size + 1
        else:
            if tail == False:
                cycle = reversed(range(0, len(req_list), partition_size))
            else:
                cycle = range(0, len(req_list), partition_size)
            for ind in cycle:
                segment_storage.append([ind, ind+partition_size])

        return req_list[segment_storage[segments-1][0]:segment_storage[segments-1][1]]

    if isinstance(segments, int) and segments * division_dec <= 1:
        return builder(segments)
    elif isinstance(segments, tuple):
        multi_segment = []
        for segment in segments:
            multi_segment.append(builder(segment))
        return multi_segment
