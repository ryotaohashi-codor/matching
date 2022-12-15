from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import generic
from django.views.decorators.http import require_POST


User = get_user_model()


class Top(LoginRequiredMixin, generic.ListView):
    template_name = 'matching/top.html'
    model = User

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        # 自分は一覧から除外 exclude(id=user.id)
        # 自分が既にいいねした人は一覧から除外 exclude(id__in=user.likes.values('id')
        queryset = queryset.exclude(id=user.id).exclude(id__in=user.likes.values('id'))
        return queryset


@require_POST
@login_required
def api_send_like(request):
    """いいねを押した際に呼ばれる"""
    id = int(request.POST['id'])
    request.user.likes.add(id)
    target = User.objects.get(id=id)

    # 相手も自分をすでに良いねしていた場合、マッチング成立なので、is_matching変数も返す
    is_matching = False
    if request.user.id in target.likes.values_list('id', flat=True):
        is_matching = True

    result = {
        'status': 200,
        'is_matching': is_matching,
    }
    return JsonResponse(result)


@require_POST
@login_required
def api_send_dislike(request):
    """いいねを取り消した場合に呼ばれる"""
    id = int(request.POST['id'])
    request.user.likes.remove(id)

    result = {
        'status': 200,
    }
    return JsonResponse(result)


class MatchingUsers(LoginRequiredMixin, generic.ListView):
    template_name = 'matching/matching_users.html'
    model = User

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        # 自分「を」いいねしている filter(likes__in=[user.id])
        # 自分「が」いいねしている filter(id__in=user.likes.values('id')
        queryset = queryset.filter(likes__in=[user.id]).filter(id__in=user.likes.values('id'))
        return queryset


class LikeUsers(LoginRequiredMixin, generic.ListView):
    template_name = 'matching/like_users.html'
    model = User

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        # 自分がいいねしている人たち
        queryset = queryset.filter(id__in=user.likes.values('id'))
        return queryset
