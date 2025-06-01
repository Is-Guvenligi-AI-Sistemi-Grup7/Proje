class SecuredOperation:
    def __init__(self, roles: str):
        self._roles = roles.split(',')
        self._http_context_accessor = ServiceTool.service_provider.get_service("IHttpContextAccessor")
    
    def on_before(self, invocation):
        role_claims = self._http_context_accessor.http_context.user.claim_roles()
        
        for role in self._roles:
            if role in role_claims:
                return
        
        raise Exception(Messages.AUTHORIZATION_DENIED)