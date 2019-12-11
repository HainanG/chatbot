# 發大柴
A Line bot based on a finite state machine  
Bot ID : @868dsjla  
QR code :  
![QRcode](img/868dsjla.png)  
## Setup

### Prerequisite
* Python 3.6
* Pipenv
* Line App
* HTTPS Server

#### Install Dependency
```sh
pip3 install pipenv

pipenv --three

pipenv install

pipenv shell
```

#### Secret Data
You should generate a `.env` file to set Environment Variables refer to our `.env.sample`.
`LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](img/show-fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* State: user
	* Input: "我要發大柴"
		* State: home
		* 有錢 Reply: "目前財產 : XXX 請選擇押注 大 或 小 或 豹子"
			* Input: "大"
				* State: big
				* 搖出豹子 Reply: "錢拿來"
				* 小於10 Reply: "輸給本汪" 
				* 大於 9 Reply: "本汪輸了"
			* Input: "小"
				* State: small
				* 搖出豹子 Reply: "錢拿來"
				* 大於 9 Reply: "輸給本汪" 
				* 小於10 Reply: "本汪輸了"
			* Input: "豹子"
				* State: wow
				* 搖出豹子 Reply: "666"
				* 沒有豹子 Reply: "還想玩大的啊"
		* 沒錢 Reply: "你破產了窮逼 , 如果給本汪罐罐本汪就給你錢錢(輸入罐罐)"

		
