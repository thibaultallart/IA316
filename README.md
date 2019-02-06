# Recommender System Project

Welcome on the AI316 Recommender System project page.

This project have to be done by team of 2.

Each week a new environment is released. 
Each environment simulate different aspect of user behavior. 
Your goal as an agent is to implement a recommender system that get the best performances on each environments.

## Environments
Each environment will be accessible through a different IP address. 
Next examples used 1.2.3.4 but make sure to use the good ones instead. 

Each environment is specific to a user session. 
Logging have been send to you by email. 

To be identified each request should contain your user_id

```http request
user_id=aaaa
``` 

### First Environment
This environment encode the classic explicit feedback setting with user, item and rating.

The first thing to do is to call the reset method.
It will initialize the environment and return a new sample of historical data

#### Reset
```http
http://35.180.46.68/reset?user_id=aaaa
```

- Restart the environment with new random values.
- Return historical data already temporally aligned.


#### Predict

Call 
```http
http://1.2.3.4/predict?user_id=aaaa&predicted_score=0.761
```

Return
```json
{"next_item":158,"next_user":25,"rating":1}
```

Require:
- user_id
- predicted_score (for previous (user, item))

Return:
- rating
- next_user
- next_item

Notice the lag here. Rating returned by the environment correspond to the previously send (user, item).

## Second environment
The second environment is a variation of the first one that include covariates in the inputs (a.k.a. content based).

Methods are the same but you receive also a vector of features.
- next_variables


## Third environment
The third environment generate implicit feedback.

To be released soon.


## Performance evaluation

### Explicit feedback environments
The performance metric will be mse over 1000 steps on 3 independent run.

### Implicit feedback environments
Those environment explicitly gives you the reward at each steps.

The performance metric will be the cumulative reward over 1000 steps on 3 independent run.


## Deploy your own API
On the first environment you're asked to develop an API that can be requested to get prediction.

We should be able to deploy this API by running only

```bash
docker compose up --build
```

Evaluation method is the same than before but we will send queries every 100ms.
Non responding request will count as +1000.



