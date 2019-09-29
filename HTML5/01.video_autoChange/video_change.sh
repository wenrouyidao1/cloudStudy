SOURCEVIDEO="/tmp/SourceVideo"
TARGETVIDEO="/var/ftp/ClassVideo"

CMD="ffmpeg -i ${SOURCEVIDEO}/${fileiawk}.mov ${TARGETVIDEO}/${fileawk}.mp4"

#1.sudo yum install epel-release
#2.sudo rpm -v --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
#3.sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
#4.sudo yum install ffmpeg ffmpeg-devel

mkdir -p /tmp/SourceVideo /var/ftp/ClassVideo
ps aux | grep ffmpeg | grep -v "grep" &>/dev/null

if [ $? -ne 0 ];then
    for file in $(ls ${SOURCEVIDEO});do
      fileawk=$(echo "${file}" | awk -F. '{ print $1 }')
      if [ -f ${TARGETVIDEO}/${fileawk}.mp4 ];then
          rm -rf ${SOURCEVIDEO}/${file}
      else
          ${CMD}
          rm -rf ${SOURCEVIDEO}/${file}
      fi
    done
fi
