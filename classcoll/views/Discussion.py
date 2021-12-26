import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from ..models import Piece, Comment, Upvote

MESSAGE_POST_COMMENT_SUCCESS = "Post comment successful"
MESSAGE_EDIT_COMMENT_SUCCESS = "Edit comment successful"
MESSAGE_DELETE_COMMENT_SUCCESS = "Delete comment successful"

@login_required(login_url='login')
@csrf_exempt
def comment(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        # id refers to piece id
        target = Piece.objects.filter(id=id).first()
        newComment = Comment.objects.create(
            user=request.user,
            content=data.get('content'),
            piece=target
        )
        newComment.save()
        return JsonResponse({'message': MESSAGE_POST_COMMENT_SUCCESS}, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        existedComment = Comment.objects.filter(
            pk = id,
            user = request.user,
        ).first()
        existedComment.content = data.get('content')
        existedComment.save()
        return JsonResponse({'message': MESSAGE_EDIT_COMMENT_SUCCESS}, status = 200)
    elif request.method == 'DELETE':
        existedComment = Comment.objects.filter(
            pk = id
        ).first()
        existedComment.delete()
        return JsonResponse({'message': MESSAGE_DELETE_COMMENT_SUCCESS}, status = 200)

@login_required(login_url='login')
@csrf_exempt
def upvote(request, id):
    if request.method == 'PUT':
        comment = Comment.objects.filter(id = id).first()
        upvoted = Upvote.objects.filter(
            user = request.user,
            comment = comment
        ).first()
        if upvoted is not None:
            upvoted.delete()
            return JsonResponse({'status': False}, status = 200)
        else:
            upvoted = Upvote.objects.create(
                user = request.user,
                comment = comment
            )
            upvoted.save()
            return JsonResponse({'status': True}, status = 200)