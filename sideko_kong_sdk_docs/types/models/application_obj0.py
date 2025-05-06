import pydantic
import typing

from .application_developers_item import ApplicationDevelopersItem
from .application_obj0_dcr_provider import ApplicationObj0DcrProvider
from .application_obj0_portal import ApplicationObj0Portal
from .auth_strategy_client_credentials import AuthStrategyClientCredentials
from .labels_update import LabelsUpdate


class ApplicationObj0(pydantic.BaseModel):
    """
    ApplicationObj0
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    auth_strategy: AuthStrategyClientCredentials = pydantic.Field(
        alias="auth_strategy",
    )
    """
    Client Credential Auth strategy that the application uses.
    """
    client_id: str = pydantic.Field(
        alias="client_id",
    )
    """
    The ID used to linked the portal application to an Identity Provider application.
    """
    created_at: str = pydantic.Field(
        alias="created_at",
    )
    """
    An ISO-8601 timestamp representation of entity creation date.
    """
    dcr_provider: typing.Optional[ApplicationObj0DcrProvider] = pydantic.Field(
        alias="dcr_provider",
    )
    """
    Information about the DCR provider this application uses, if using DCR.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description",
    )
    """
    A description of the application.
    """
    developers: typing.List[ApplicationDevelopersItem] = pydantic.Field(
        alias="developers",
    )
    """
    List of developers that have access to this application.
    """
    granted_scopes: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="granted_scopes",
    )
    """
    List of granted scopes for the application. Null if application type does not support returning granted scopes.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Contains a unique identifier used for this resource.
    """
    labels: typing.Optional[LabelsUpdate] = pydantic.Field(
        alias="labels",
    )
    """
    Labels store metadata of an entity that can be used for filtering an entity list or for searching across entity types. 
    
    Labels are intended to store **INTERNAL** metadata.
    
    Keys must be of length 1-63 characters, and cannot start with "kong", "konnect", "mesh", "kic", or "_".
    
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The name of the application.
    """
    portal: ApplicationObj0Portal = pydantic.Field(
        alias="portal",
    )
    """
    Information about the portal the application is in.
    """
    registration_count: float = pydantic.Field(
        alias="registration_count",
    )
    """
    The number of API registrations that are associated with the application. Registrations of any status are included in the count.
    """
    updated_at: str = pydantic.Field(
        alias="updated_at",
    )
    """
    An ISO-8601 timestamp representation of entity update date.
    """
