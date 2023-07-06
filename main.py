from youtube_statistics import YTstats
API_KEY = "AIzaSyBsC4LNKhLzvJopvnYclDF8A5GUr-xrRkc"
channel_id ="UC2UXDak6o7rBm23k3Vv5dww" 
yt = YTstats(API_KEY,channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()
#yt.get_channel_video_data()