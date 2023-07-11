from django.shortcuts import render,HttpResponse,redirect
from .models import Post,BlogComment
from django.contrib import messages
from blog.templatetags import poll_extras

# Create your views here.

def blogHome(request):
    allPost = Post.objects.all()
    content = {'allPost' : allPost}
    # print(content)
    return render(request,'blog/blogHome.html',content)


def blogPost(request,slug):
    post = Post.objects.filter(slug=slug)[0]
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    # print('comment',comments,'replies', replies)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context = {'post':post,'comments':comments,'user':request.user,'replyDict':replyDict}
    return render(request,'blog/blogPost.html',context)



def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user 
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno == '':
            comment = BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,'Your comment has been successfully posted')
        else: 
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request,'Your reply has been posted')


    return redirect(f'/blog/{post.slug}')