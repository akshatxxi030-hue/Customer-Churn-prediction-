from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated,ClassVar,Dict
class user_input(BaseModel):
    age:Annotated[int,Field(...,ge=0,le=100)]
    region:Annotated[str,Field(...,description="Enter the region user belongs to")]
    watch_hours:Annotated[float,Field(...,description="Enter the monthly watch time")]
    subscription_type:Annotated[Literal["Basic","Standard","Premium"],Field(...,description="Enter the subscription type")]
    number_of_profiles:Annotated[int,Field(...,ge=1,le=5,description="Enter the number of profiles user has")]
    gender:Literal["Male","Female","Other"]="Other"
    device:Literal['TV', 'Mobile', 'Laptop', 'Desktop', 'Tablet']="Tablet"
    payment_method:Literal['Gift Card', 'Crypto', 'Debit Card', 'PayPal', 'Credit Card']="Debit Card"
    favorite_genre:Literal['Action', 'Sci-Fi', 'Drama', 'Horror', 'Romance', 'Comedy','Documentary']="Documentary"
    
    monthly_price_map:ClassVar[Dict[str,float]]={
    "Basic":8.99,
    "Standard":13.99,
    "Premium":17.99
}
    @computed_field
    @property
    def avg_watch_time_per_day(self) ->float:
        return self.watch_hours/30
    
    @computed_field
    @property
    def monthly_fee(self) -> float:
        return self.monthly_price_map[self.subscription_type]