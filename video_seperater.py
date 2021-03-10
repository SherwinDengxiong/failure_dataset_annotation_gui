import cv2
import os



def videotoframe(videofilepath,outputfilepath,videoname):
    cap = cv2.VideoCapture(videofilepath)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = cap.get(cv2.CAP_PROP_FPS)
    # fps=30
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    # size=(960,544)
    i = 0
    while (cap.isOpened()):
        i = i + 1
        ret, frame = cap.read()
        num=str(i).zfill(6)

        if ret == True:
            cv2.imwrite(outputfilepath+ os.path.sep + num + '.jpg', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()

    cv2.destroyAllWindows()
def main():
    videodatasetpath='E:/failure/failuredata'
    videospath='E:/failure/videos'
    for i in os.listdir(videodatasetpath):

        sectionvideopath=videodatasetpath+os.path.sep+i
        sectionname=i
        for j,filename in enumerate(os.listdir(sectionvideopath)):

            newfilename=sectionname+'_'+str(j)
            outnewfilepath=videospath+os.path.sep+newfilename
            # if not os.path.exists(outnewfilepath):
            #     os.mkdir(outnewfilepath)
            # else:
            #     continue

            videoFile = sectionvideopath+os.path.sep+filename
            # print(outnewfilepath)
            outputFile = outnewfilepath
            videoname=filename
            # print(videoFile)
            # namechangedpath=sectionvideopath+os.path.sep+sectionname
            # print(namechangedpath)
            # os.rename(videoFile,videoFile+'.mp4')


        # videoname='beauty1'
        #     videotoframe(videoFile,outputFile,videoname)
if __name__ == '__main__':
    main()