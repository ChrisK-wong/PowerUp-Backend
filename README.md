# PowerUp Backend

## Using the API

API: [power-up-backend.vercel.app](power-up-backend.vercel.app)

## Recommendations

### foods
| Endpoint   | HTML Parameters | Returns | Sample Request |
|------------|-----------------|---------|----------------|
| /api/foods/{type}<br><br/>types:<br><br/>`calorie`<br/>`protein`<br/>`carbs`<br/>`fiber`<br/>`fat`| min: int<br>max: int<br>limit: int | Returns JSON list of foods and nutritional information given the parameters | https://power-up-backend.vercel.app/api/foods/calories?min=100&max=200&limit=1 |

### exercise
| Endpoint   | HTML Parameters | Returns                                                | Sample Request |
|------------|-----------------|--------------------------------------------------------|----------------|
| /api/exercise/{type}<br><br/>types:<br><br/>`cardio`<br/>`flexibility`<br/>`arms`<br/>`core`<br/>`legs` | limit: int      | Returns JSON list of exercise obj relating to the type | https://power-up-backend.vercel.app/api/foods/calories?min=100&max=200&limit=1 |

## Scoring

### health score
| Endpoint   | HTML Parameters | Returns                                               | Sample Request |
|------------|-----------------|-------------------------------------------------------|----------------|
| /api/score/health | gender: int<br/>height: int<br/>weight: int | <pre lang="json">{&#13;    "health_score": 0.8&#13;}</pre> | [https://power-up-backend.vercel.app/api/score/health?gender=0&height=180&weight=60](https://power-up-backend.vercel.app/api/score/health?gender=0&height=180&weight=60) |
