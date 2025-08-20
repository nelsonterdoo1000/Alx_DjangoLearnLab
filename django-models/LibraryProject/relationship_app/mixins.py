from django.http import HttpResponseForbidden

class RoleRequiredMixin:
    allowed_roles = []
    
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            user_role = request.user.profile.role
            if user_role in self.allowed_roles:
                return super().dispatch(request,*args,**kwargs)
        return HttpResponseForbidden("You do not have permission to View this page")