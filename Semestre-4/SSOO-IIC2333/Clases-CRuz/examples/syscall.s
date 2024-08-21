	.file	"syscall.c"
	.text
	.globl	main
	.type	main, @function
main:
.LFB2:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movl	%edi, -20(%rbp)
	movq	%rsi, -32(%rbp)
	movl	$186, %edi
	movl	$0, %eax
	call	syscall
	movl	%eax, -4(%rbp)
	call	getpid
	movl	%eax, %esi
	movl	-4(%rbp), %eax
	movl	$1, %ecx
	movl	%eax, %edx
	movl	$234, %edi
	movl	$0, %eax
	call	syscall
	movl	%eax, -4(%rbp)
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
