#coding:utf-8
import time
import os

text_line = """
        <tr>
            <td>
                <a href="{href}"> {name} </a>
            </td>
            <td>
                {date}
            </td>
        </tr>
"""

video_line = """
        <div class="col-md-4">
            <div class="thumbnail">
                <video src="{file}"
                       width="355" height="200"
                       loop
                       muted
                       controls="controls">
                    对不起！ 您的浏览器不支持，请升级
                </video>
                <div class="caption">
                    <h3>
                        {name}
                    </h3>
                </div>
            </div>
        </div>
"""

index_tem = open("indexModule.html", encoding='utf8').read()
detail_tem = open("detail.html", encoding='utf8').read()


def index(path="video"):
    lines = ""
    Date = os.stat(path).st_atime
    time_local = time.localtime(Date)
    for sub_dir in os.listdir(path):
        lines += text_line.format(href=sub_dir + ".html",
                                  name=sub_dir,
                                  date=time.strftime('%Y-%m-%d %H:%M:%S', time_local)
                                  )
    with open("indexModule.html", "w", encoding='utf8') as f:
        f.write(index_tem.format(lines=lines))


def detail(path="video"):
    for sub_dir in os.listdir(path):
        lines = ""
        abs_sub_dir = os.path.join(path, sub_dir)
        for video in os.listdir(abs_sub_dir):
            abs_file = os.path.join(abs_sub_dir, video)
            lines += video_line.format(name=video,
                                       file=abs_file
                                       )
        else:
            with open(sub_dir + ".html", "w", encoding='utf8') as f:
                f.write(detail_tem.format(lines=lines))


if __name__ == "__main__":
    index()
    detail()
