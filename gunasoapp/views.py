from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import GunasoForm
from .models import Gunaso

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


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.html import format_html
from .forms import GunasoForm

def submit_report(request):
    if request.method == "POST":
        form = GunasoForm(request.POST)
        if form.is_valid():
            form.save()

            # Get the form data
            form_data = form.cleaned_data

            # Create a mapping for field names to more readable labels
            field_labels = {
                'description': 'Description',
                'incident_date': 'Incident Date',
                'incident_location': 'Incident Location',
            }

            # Construct the HTML email message
            message = format_html(
                """
                <html>
                <body>
                    <p>A Whistle Blower report has been submitted with the following details:</p>
                    <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse;">
                        <thead>
                            <tr>
                                <th><strong>Report</strong></th>
                                <th><strong>Data</strong></th>
                            </tr>
                        </thead>
                        <tbody>
                """
            )

            for field, value in form_data.items():
                readable_field = field_labels.get(field, field)
                message += format_html(
                    """
                    <tr>
                        <td><strong>{}</strong></td>
                        <td>{}</td>
                    </tr>
                    """, readable_field, value
                )

            message += format_html(
                """
                        </tbody>
                    </table>
                </body>
                </html>
                """
            )

            # Send email notification with HTML content
            send_mail(
                'New Whistle Blower Report Submitted',
                '',  # Plain text message (empty in this case)
                'noreplywhistle@adbl.gov.np',
                ['adminwb1@adbl.gov.np','adminwb2@adbl.gov.np'],
                fail_silently=False,
                html_message=message  # Specify the HTML message here
            )
            messages.success(request, 'Message sent successfully!')
            return redirect('submit_report')
        else:
            # Print form errors to the console
            print(form.errors)
    else:
        form = GunasoForm()

    return render(request, 'report_form.html', {'form': form})

@login_required
#@user_passes_test(lambda u: u.is_staff)
def report_final(request):
    reports = Gunaso.objects.all().order_by('-submitted_at')  # Get all reports and order them by submission date
    paginator = Paginator(reports, 25)  # Show 10 reports per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'report_final.html', {'page_obj': page_obj})