import requests
import json
request = requests.get(
    'https://www.dcard.tw/_api/forums/pet/posts?popular=true')
target_arrays = json.loads(request.text)

for target_array in target_arrays:
    print('標題:{0:30s}貼文時間:{1:20s}留言人數:{2:4d}:4}按讚人數:{3:4d}'.format(
        target_array['title'], target_array['createdAt'], target_array['commentCount'], target_array['likeCount']))
