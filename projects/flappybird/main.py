import sys,turtle,pygame,random
num=0
class Bird(object):
    def __init__(self):
        self.birdRect=pygame.Rect(65,50,50,50)
        a=random.choice([1,4,7])
        self.birdStatus=[pygame.image.load(str(a)+".png"),
                        pygame.image.load(str(a+1)+".png"),
                        pygame.image.load(str(a+2)+".png")]
        self.dead=False
        self.status=0
        self.birdX=120
        self.birdY=350
        self.jump=False
        self.jumpSpeed=10
        self.gravity=5
        
        
    def birdUpdate(self):
        global num
        self.birdStatus
        num+=1
        self.status=num%3
        if self.jump:
            self.jumpSpeed-=0.5
            self.birdY-=self.jumpSpeed
        else:
            self.gravity+=0.2
            self.birdY+=self.gravity
            
        self.birdRect[1]=self.birdY



class Pipeline(object):
    def __init__(self):
        self.wallx=400
        self.wally=random.randint(-100,0)
        s=random.randint(1,2)
        aUp=pygame.image.load("p"+str(s)+".png")
        self.pineUp=pygame.transform.flip(aUp,False,True)
        self.pineDown=pygame.image.load("p"+str(s)+".png")

        
    def updatePipeline(self):
        global score
        self.wallx-=5
        if self.wallx==20 and not Bird.dead:
            score+=1
            sound1.play()
        if self.wallx<-80:
            self.wally=random.randint(-100,0)
            self.wallx=400
            

def createMap():
    
    screen.fill((255,255,255))
    screen.blit(background,(0,0)) 
    #管道
    screen.blit(Pipeline.pineUp,(Pipeline.wallx,Pipeline.wally))
    screen.blit(Pipeline.pineDown,(Pipeline.wallx,Pipeline.wally+500))
    Pipeline.updatePipeline()
    #鸟
    if Bird.dead:
        Bird.status=2
    screen.blit(Bird.birdStatus[Bird.status],(Bird.birdX,Bird.birdY))
    Bird.birdUpdate()
    #分数
    screen.blit(font.render(str(score),-1,(255,255,255)),(190,50))
    pygame.display.update()

def checkDead():
    upRect=pygame.Rect(Pipeline.wallx,Pipeline.wally,Pipeline.pineDown.get_width()-20,Pipeline.pineDown.get_height()-5)
    downRect=pygame.Rect(Pipeline.wallx,Pipeline.wally+500,Pipeline.pineDown.get_width()-20,Pipeline.pineDown.get_height()-5)
    if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
        Bird.dead=True
    if not 0<Bird.birdRect[1]<height:
        Bird.dead=True
        
        return True
    else:
        return False

def getResult():
    final_text1="Good game"
    final_text2="Your final score is:"+str(score)
    ft1_font=pygame.font.SysFont("微软雅黑",70)
    ft1_surf=font.render(final_text1,1,(242,3,36))
    ft2_font=pygame.font.SysFont("微软雅黑",50)
    ft2_surf=font.render(final_text2,1,(253,177,6))
    screen.blit(ft1_surf,[(screen.get_width()-ft1_surf.get_width())/2,100])
    screen.blit(ft2_surf,[(screen.get_width()-ft2_surf.get_width())/2,200])
    pygame.display.flip()
    
    
flag=True
if __name__=="__main__":
    
    pygame.init()
    font=pygame.font.SysFont(None,50)
    size=width,height=400,650
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption("小饼干")
    clock=pygame.time.Clock()
    Pipeline=Pipeline()
    Bird=Bird()
    sound1=pygame.mixer.Sound("point.wav")
    sound2=pygame.mixer.Sound("hit.wav")
    score=0
    ss=random.randint(1,2)
    
    key=False
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                # sys.exit()
                pygame.quit()
                print("点击左侧运行重新开始\n")
                sys.exit()
            if(event.type==pygame.KEYDOWN or event.type==pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                key =True
                Bird.jump=True
                Bird.gravity=5
                Bird.jumpSpeed=10
        if key:
            background=pygame.image.load("bg"+str(ss)+".png")
            background=pygame.transform.scale(background,(400,650))
            if checkDead():
                getResult()
                if flag:
                    sound2.play()
                    flag=not flag
            else:
                createMap()
        else:
            a=pygame.image.load("bg"+str(ss)+".png")
            background1=pygame.transform.scale(a,(400,650))
            b=pygame.image.load("message.png")
            background=pygame.transform.scale(b,(184,267))
            screen.blit(background1,(0,0))
            screen.blit(background,((400-184)/2,(650-267)/2))
            screen.blit(Bird.birdStatus[Bird.status],(Bird.birdX,Bird.birdY))
            pygame.display.update()
    
