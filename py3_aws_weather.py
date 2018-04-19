import time
import py3_weather_click as weather
import py3_aws_click as aws


def setup():
    aws.resetaws()

    aws.setup()
    print("AWS  open")
    
    weather.setup()

def run():
    setup()

    while True:
        jsonmsg = ""
        jsonmsg = weather.getdata(jsonmsg)

        # send data length
        aws.sendcmd(aws.publish % len(jsonmsg))
        aws.recvdata('>')    

        # send data
        aws.sendcmd(jsonmsg)
        aws.recvdata(aws.ok)

        # wait for time to send next message
        time.sleep(30)

    ser.close()

if __name__=="__main__":
    run()
