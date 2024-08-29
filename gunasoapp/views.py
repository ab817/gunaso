from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import GunasoForm


def home(request):
    form = GunasoForm()  # Initialize the form

    if request.method == "POST":
        confirmation = request.POST.get('confirmation')

        if confirmation == 'yes':  # If the 'Yes' button is clicked
            return redirect('submit_report')
        elif confirmation == 'no':  # If the 'No' button is clicked
            # Optionally add a message or keep the user on the same page
            return render(request, 'home.html',  {'form': form})

    return render(request, 'home.html',  {'form': form})


def submit_report(request):
    if request.method == "POST":
        form = GunasoForm(request.POST)
        if form.is_valid():
            form.save()

            # Get the form data
            form_data = form.cleaned_data

            # Create a message with the form data
            message = "A Whistle Blower report has been submitted with the following details:\n"
            for field, value in form_data.items():
                message += f"{field}: {value}\n"

            # Send email notification
            send_mail(
                'New Whistle Blower Report Submitted',
                message,
                'ablive817@gmail.com',
                ['ablive09@gmail.com'],
                fail_silently=False,
            )

            return render(request, 'confirmation.html')
        else:
            # Print form errors to the console
            print(form.errors)
    else:
        form = GunasoForm()

    return render(request, 'report_form.html', {'form': form})
