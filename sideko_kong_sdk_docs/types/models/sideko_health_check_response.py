import pydantic


class SidekoHealthCheckResponse(pydantic.BaseModel):
    """
    SidekoHealthCheckResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ok: bool = pydantic.Field(
        alias="ok",
    )
