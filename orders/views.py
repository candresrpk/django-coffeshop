from django.views.generic import DetailView, CreateView
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderProductForm
from django.urls import reverse_lazy
# Create your views here.

class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/my_orders.html'
    context_object_name = 'order'
    
    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = 'orders/create_order.html'
    form_class = OrderProductForm
    success_url = reverse_lazy('orders:my_orders')
    
    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            is_active=True,
            user = self.request.user
        )
        
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
    