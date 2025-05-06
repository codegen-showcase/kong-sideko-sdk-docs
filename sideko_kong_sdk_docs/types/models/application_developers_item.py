import pydantic


class ApplicationDevelopersItem(pydantic.BaseModel):
    """
    ApplicationDevelopersItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
